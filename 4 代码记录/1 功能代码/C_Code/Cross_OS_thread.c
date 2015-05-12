
#include<stdio.h>

#ifdef WIN32
    #include<windows.h>
#else
    #include<pthread.h>
#endif

#ifndef WIN32
    #define THREAD_FUN_DEF(fun_name,parm) \
        void *fun_name(void *parm)
    #define THREAD_HANDLE_ID pthread_t
    #define THREAD_CREATE_MIC(handle ,fun_name,parm) \
        pthread_create(&handle,NULL,fun_name,(void*)&parm)
    #define THREAD_END() pthread_detach(pthread_self())
    #define MSLEEP(x)  sleep(x)
#else
    #define THREAD_FUN_DEF(fun_name,parm) \
        WINAPI DWORD fun_name(LPVOID parm)
    #define THREAD_HANDLE_ID HANDLE
    #define THREAD_CREATE_MIC(handle,fun_name,parm) \
        CreateThread(NULL,0,fun_name,(void*)&parm,0,NULL)
    #define THREAD_END() Sleep(1)
    #define MSLEEP(x)  Sleep(x*1000)
#endif

THREAD_FUN_DEF(test_fun,p_num){
    int num = *(int *)p_num;
    int i = 0;
    while(i < 1000){
        i++;
        printf("[%d] times is %d\n",i,num);
        MSLEEP(1);
    }
    THREAD_END();
    return 0;
}

int main(){
   THREAD_HANDLE_ID thread_1; 
   int poolnum = 20;
   if( THREAD_CREATE_MIC(thread_1,test_fun,poolnum) < 0){
        printf("Error thread create \n");
        return -1;
    }
    while(1){
        MSLEEP(1000);
    };
    return 0;
}

