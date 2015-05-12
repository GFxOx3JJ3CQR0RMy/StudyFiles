function Myswap(a,i,j) {
	var buf = a[i];
	a[i] = a[j];
	a[j] = buf;
}

function reverse(a,i,j){
	var i1 = i;
	var j1 = j;
	while (i1 < j1){
		Myswap(a,i1,j1);
		i1 += 1;
		j1 -= 1;
	}
}

function getlist(a,n,b){
	var result = []
	for (var i in a ){
		result.push(b[a[i]]);
	}
	return result;
}

function combination(b,n,BackFun){
	var num = 0;
	if ( n < 2)  return ;
	var i = 0;
	var a = []
	while ( i < n ) {a.push (i) ; i += 1; }
	while ( true ){
		BackFun(getlist(a,n,b));
		num += 1;
		console.log(num);
		i = n - 2
		while( i >= 0){
			if( a[i] < a[i+1]) break;
			else if ( i == 0 ) return ;
			i -= 1;
		} 
		j = n - 1;
		while ( j > i ){
			if (a[j]> a[i])  break;
			j -= 1;
		}
		Myswap(a,i,j)
		reverse(a,i+1,n-1)
	}  
}

function  CallBacktest(newStr){
	console.log(newStr.toString());
}

var list = ['a','b','c','d','e'];
combination(list,5,CallBacktest);