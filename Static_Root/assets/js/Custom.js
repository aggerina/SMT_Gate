
function SendArticleComment(article_id) {
    // console.log("clicket comment")
    var article_comment = $('#Comment_text').val();
    var  parent_id = $('#parent_id').val();

    $.get('/articles/add_article_comment', {
        article_id: article_id,
        article_comment,
        parent_id:parent_id,


    }).then(res => {

        $('#comment_area').html(res);
        $('#Comment_text').val('');
        $('#parent_id').val('');

        if(parent_id !== null && parent_id !== '') {
            document.getElementById('SelfComment'+ parent_id).scrollIntoView({behavior:"smooth"});
        } else {
            document.getElementById('comment_area').scrollIntoView({behavior:"smooth"});
        }
    })

}

function  FillParentID(parent_id){
    $('#parent_id').val(parent_id);
    // window.scroll()
    document.getElementById('comment_for').scrollIntoView({behavior:"smooth"});
}








function SendNewsComment(news_id) {
    // console.log("clicket comment")
    var news_comment = $('#Comment_text').val();
    var  parent_id = $('#parent_id').val();

    $.get('/news/add_news_comment', {
        article_id: news_id,
        news_comment,
        parent_id:parent_id,


    }).then(res => {


        $('#comment_area').html(res);
        $('#Comment_text').val('');
        $('#parent_id').val('');

        if(parent_id !== null && parent_id !== '') {
            document.getElementById('SelfComment'+ parent_id).scrollIntoView({behavior:"smooth"});
        } else {
            document.getElementById('comment_area').scrollIntoView({behavior:"smooth"});
        }
    })

}

function  FillparentID(parent_id){
    $('#parent_id').val(parent_id);
    // window.scroll()
    document.getElementById('comment_for').scrollIntoView({behavior:"smooth"});
}