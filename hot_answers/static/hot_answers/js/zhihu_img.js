function addPrefix(group) {
    group.each(function() {
        var src = "http:" + $(this).attr("src");
        $(this).attr("src", src);
    });
}

$(document).ready(function() {
    // add prefix http: to image sources
    addPrefix($("img"));
});