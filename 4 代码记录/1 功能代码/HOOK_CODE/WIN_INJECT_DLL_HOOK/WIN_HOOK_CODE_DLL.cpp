// dllmain.cpp : 定义 DLL 应用程序的入口点。
#include "stdafx.h"

#include "windows.h"
#include "tchar.h"

#pragma comment(lib, "urlmon.lib")

#define DEF_URL     	(L"http://www.naver.com/index.html")
#define DEF_FILE_NAME   (L"index.html")



HMODULE g_hMod = NULL;

BYTE g_pMCTF[5] = {0,};
BYTE pBuf[5] = {0xE9, 0, };
FARPROC CreateFile_Addr;

void DebugLog(const char *format, ...)
{
	va_list vl;
	FILE *pf = NULL;
	char szLog[512] = {0,};

	va_start(vl, format);
	wsprintfA(szLog, format, vl);
	va_end(vl);

    OutputDebugStringA(szLog);
}



HANDLE WINAPI MyCreateFile(  
        __in          LPCSTR lpFileName,  
        __in          DWORD dwDesiredAccess,  
        __in          DWORD dwShareMode,  
        __in          LPSECURITY_ATTRIBUTES lpSecurityAttributes,  
        __in          DWORD dwCreationDisposition,  
        __in          DWORD dwFlagsAndAttributes,  
        __in          HANDLE hTemplateFile  
        )  
{  
    MessageBox(0,L"MyCreateFile",L"Test",0);  
    //恢复API头8个字节  
    WriteProcessMemory( INVALID_HANDLE_VALUE, (void*)CreateFile_Addr,  
        (void*)g_pMCTF, 5, NULL);  
  

	MessageBox(0,(LPCWSTR)lpFileName,L"Test",0);  
 //   printf("lpFileName is %s\n",lpFileName);  
  
    //调用正确的函数  
    HANDLE hFile=CreateFileA(lpFileName,dwDesiredAccess,dwShareMode,  
        lpSecurityAttributes,dwCreationDisposition,dwFlagsAndAttributes,hTemplateFile);  
          
    //写入跳转语句，继续Hook  
       WriteProcessMemory(INVALID_HANDLE_VALUE, (void*)CreateFile_Addr,  
       (void*)pBuf, 5, NULL);  
  
    return hFile;  
}  


int WINAPI MyMessageBox(HWND hWnd,LPCSTR lpText,LPCSTR lpCaption,UINT uType)  
{  
	int result;
	WriteProcessMemory( INVALID_HANDLE_VALUE, (void*)CreateFile_Addr,  
        (void*)g_pMCTF, 5, NULL);  
	result = MessageBox(0,L"This Message say by HOOK ! \n",L"HOOK",uType);
//	MessageBox(hWnd,(LPCWSTR)lpText,(LPCWSTR)lpCaption,uType);
	WriteProcessMemory(INVALID_HANDLE_VALUE, (void*)CreateFile_Addr,  
       (void*)pBuf, 5, NULL);  
    return result;  
}  

BOOL hook_by_code(LPCSTR szDllName, LPCSTR szFuncName, PROC pfnNew, PBYTE pOrgBytes)
{
	FARPROC pFunc = NULL;
	DWORD dwOldProtect = 0, dwAddress = 0;
	
	PBYTE pByte = NULL;
    HMODULE hMod = NULL;

    hMod = GetModuleHandleA(szDllName);
    if( hMod == NULL )
    {
		DebugLog("Not found The DLL \n");
        return FALSE;
    }

	pFunc = (FARPROC)GetProcAddress(hMod, szFuncName);
    if( pFunc == NULL )
    {
		DebugLog("Not Found The Fun\n");
        return FALSE;
    }

	pByte = (PBYTE)pFunc;
	CreateFile_Addr = pFunc;
	if( pByte[0] == 0xE9 )
    {
        DebugLog("hook_by_code() : The API is hooked already!!!\n");
		return FALSE;
    }

	if( !VirtualProtect((LPVOID)pFunc, 5, PAGE_EXECUTE_READWRITE, &dwOldProtect) )
    {
        DebugLog("hook_by_code() : 111111 failed!!! [%d]\n", GetLastError());
        return FALSE;
    }

	memcpy(pOrgBytes, pFunc, 5);

	dwAddress = (DWORD)pfnNew - (DWORD)pFunc - 5;
	memcpy(&pBuf[1], &dwAddress, 4);

	memcpy(pFunc, pBuf, 5);

	if( !VirtualProtect((LPVOID)pFunc, 5, dwOldProtect, &dwOldProtect) )
    {
        DebugLog("hook_by_code() : 22222222222 failed!!! [%d]\n", GetLastError());
        return FALSE;
    }
	DebugLog("HOOK OK ????\n");
	return TRUE;
}



BOOL unhook_by_code(LPCSTR szDllName, LPCSTR szFuncName, PBYTE pOrgBytes)
{
	FARPROC pFunc = NULL;
	DWORD dwOldProtect = 0;
	PBYTE pByte = NULL;
    HMODULE hMod = NULL;

    hMod = GetModuleHandleA(szDllName);
    if( hMod == NULL )
    {
        DebugLog("unhook_by_code() : GetModuleHandle(\"%s\") failed!!! [%d]\n",
                  szDllName, GetLastError());
        return FALSE;
    }

	pFunc = (FARPROC)GetProcAddress(hMod, szFuncName);
    if( pFunc == NULL )
    {
        DebugLog("unhook_by_code() : GetProcAddress(\"%s\") failed!!! [%d]\n",
                  szFuncName, GetLastError());
        return FALSE;
    }

	pByte = (PBYTE)pFunc;
	if( pByte[0] != 0xE9 )
    {
        DebugLog("unhook_by_code() : The API is unhooked already!!!");
        return FALSE;
    }

	if( !VirtualProtect((LPVOID)pFunc, 5, PAGE_EXECUTE_READWRITE, &dwOldProtect) )
    {
        DebugLog("unhook_by_code() : VirtualProtect(#1) failed!!! [%d]\n", GetLastError());
        return FALSE;
    }

	memcpy(pFunc, pOrgBytes, 5);

	if( !VirtualProtect((LPVOID)pFunc, 5, dwOldProtect, &dwOldProtect) )
    {
        DebugLog("unhook_by_code() : VirtualProtect(#2) failed!!! [%d]\n", GetLastError());
        return FALSE;
    }

	return TRUE;
}



DWORD WINAPI ThreadProc(LPVOID lParam)
{

	MessageBox(NULL,L"From Remote Thread !",L"test",0);
	hook_by_code("user32.dll","MessageBoxA",(PROC)MyMessageBox,g_pMCTF);
    return 0;
}

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved)
{
    HANDLE hThread = NULL;

    g_hMod = (HMODULE)hinstDLL;

    switch( fdwReason )
    {
    case DLL_PROCESS_ATTACH : 
        OutputDebugString(L"<myhack.dll> Injection!!!");
        hThread = CreateThread(NULL, 0, ThreadProc, NULL, 0, NULL);
        CloseHandle(hThread);
        break;
    }

    return TRUE;
}