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

$(document).ready(function() {
    // adjust the height of the thumbnails dynamically
    setHeight($(".thumbnail"));
});
