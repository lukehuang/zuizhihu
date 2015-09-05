function setHeight(group) {
    var maxHeight = 0;
    group.each(function() {
        var height = $(this).height();
        if(height > maxHeight) {
            maxHeight = height;
        }
    });

    group.each(function() {
        $(this).height(maxHeight * 1.1);
    });
}

function addPrefix(group) {
    group.each(function() {
        var src = "http:" + $(this).attr("src");
        $(this).attr("src", src);
    });
}

$(document).ready(function() {
    // add prefix http: to image sources
    addPrefix($("img"));

    // adjust the height of the thumbnails dynamically
    setHeight($(".thumbnail"));
});
