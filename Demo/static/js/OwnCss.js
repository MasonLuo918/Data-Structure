/**
 * Created by 10668 on 2018/10/18.
 */



function sleep(n) {
    var start=new Date().getTime();
    while (true) if (new Date().getTime()-start>n) break;
}
function publish_article() {
     var title = $("#id_title").val();
     var column_id = $("#which_column").val();
     var body = $("#id_body").val();
     $.ajax({
         url:"/BlogPost/article-post/",
         type:"POST",
         data:{"title":title,"body":body,"column_id":column_id},
         success:function (e) {
             if (e=="1"){

                 window.location.href="/BlogPost/PostManage/";
             }
             else if (e=="2"){
                 layer.msg("抱歉，发布失败！");
             }
             else{
                 layer.msg("项目名称必须填写，不能为空");
             }
         }
     })
}


function functionDoesNotbuild() {
      layer.msg("功能正在开发中，敬请期待！");
}

function personInformation() {
      var index=layer.open({
          type:2,
          content:'/BlogPost/PersonalInformations',
          area:["350px","400px"],
          btn:["确定"],
          btnAlign:"c",
          yes:function (index,layero) {
              layer.close(index);
          }
      });
}