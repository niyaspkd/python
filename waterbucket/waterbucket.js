var seen={}
var queue=[]
var fill=[]
function getstate(){
 global queue
 if not queue
    return None
    var state = queue[0][0]
    var queue = queue.slice(1,queue.length)
}
    return state
function addstate(parent,new){
    if var str(new) in seen
        return
    seen[str(new)]= str(parent)
    queue.push(new)
    fill.push(new)
}
function getsolution(){
    var solution=[]
    var state=
