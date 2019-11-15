$(function () {
    //====创建XMLHttpRequest/ActiveX对象====
    var xhr
    if (window.ActiveXObject){
        xhr=new ActiveXObject('Microsoft.XMLHTTP')
    } else if (window.XMLHttpRequest){
        xhr=new XMLHttpRequest()
    }
    $('#name').click(function () {
        var url='{%'
        xhr.open('post',)
    })
})