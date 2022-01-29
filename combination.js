dic={"c1":[1,2,3],"c2":[5,6,7],"c3":[9,10,11]}
c=0
function a(){
  string=" "  
for(i in dic){
  
    result=(dic[i][c]);
    st_result=result.toString()
    string=string+" "+st_result
    
    
}console.log(string);}
function b(){
    a()
c=c+1   
}
b()
b()
b()

// output:-
// 1,5,9
// 2,6,10
// 3,7,11

