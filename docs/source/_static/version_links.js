function replaceVersionURL(version) {
    var url = window.location.href;
    url = url.replace(/latest|(\d+\.\d+\.\d)/, version);
    return url;
}

function generateHTML(versions_file) {
    var request = new XMLHttpRequest();
    request.open("GET", versions_file);
    request.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var allLines = request.responseText.split(/\r\n|\n/);
            create_list(allLines);
        } else if (this.readyState == 4 && this.status == 404) {
            // HACK: For the source files in a subfolder
            generateHTML('../../available_versions.txt');
        }
    };
    request.send();

}

function create_list(version_numbers) {
    var menu = document.getElementsByClassName('wy-menu wy-menu-vertical')[0];
    var p = document.createElement('p');
    p.appendChild(document.createTextNode("All versions"));
    p.className = 'caption';
    p.style.color = '#009374';
    var ul = document.createElement('ul');
    menu.insertBefore(ul, menu.firstChild);
    menu.insertBefore(p, ul);
    version_numbers.forEach(create_list_item);
    function create_list_item(version_number) {
        var li = document.createElement('li');
        var a = document.createElement('a');
        var linkText = document.createTextNode(version_number);
        a.appendChild(linkText);
        a.href = replaceVersionURL(version_number);

        li.appendChild(a);
        ul.appendChild(li);
    }
}

window.onload = function() {
    generateHTML('../available_versions.txt');    
};
