////////   调用示例往下看 

function getlist( table , list){
    resu = [];
    for ( var p in table ){
        if(table[p] == 1){
            resu.push(list[p]);
        }
    }
    return resu
}

function newswap( table , n , m){
    //  [ 0 1 1 1 0 ]
    var i = 0;
    var j = 0;
    var flag = false;
    while (i < (n - 1)){
        if (table[ i ] == 1 &&table[ i+1 ] == 0){            
            table[ i+1 ] =1;
            table[  i ] = 0;
            ////   [ 0 1 10 1]
            var k = 0;
            while ( k < j ) {table[ k ] = 1 ; k += 1; }
            while ( k < i ) {table[ k ] = 0 ; k += 1; }
            return true;
        }
        if (table[i] == 1){
            j += 1;
        }
i += 1;
    }
     //// way out
    return false;   
    
}

//////  外部调用接口
function CNM( listTable , n , m , callBack )
{   //   CNM( ['a','b','c','d','e']  , 5 ,3 ,callBack)
    var i = 0;
    var table = [];
    if (n<m){
        console.log('ERROR n <m');
    } 
    ////     [ 1 , 1 , 1 , 0 , 0 ]
    while ( i < m ){ table.push(1); i += 1;}
    while ( i < n  ){ table.push(0); i += 1;}
    var testlist = getlist(table, listTable );
    callBack( testlist );

    while(newswap(table,n)){
        //// Every Move 1 0
        var testlist = getlist(table,listTable ); 
        callBack( testlist );
    } 
}
//////   对于每一个组合结果 执行callback操作  以回调函数方式处理
function callback(list){
    console.log( list.toString() );
}


///////  main()   一个调用示例
            ///// 在列表的 5个元素中选择3个元素，对于每种情况都调用 callback 函数 
list_table = ['a', 'b' , 'c' , 'd' , 'e'];
CNM(list_table , 5 , 3 , callback);