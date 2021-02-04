// $('#loading').modal('show');

function create_row(text, solved)
{
    console.log(text, solved)
    t = ""
    t += "<tr>"
    t += "<td>"+text+":"+"</td>"
    t += "<td>"+String(solved)+"</td>"
    t += "</tr>"
    console.log(t)
    $("table").append(t)
}

var total_counter = {};
var oj_counter = {};

var res;
$.ajax({
    url: "/frontend/query",
    type: "get",
    async: false,
    data: "",
    success: function (data) {
        res = data;
    }
});

console.log(res);
var records = JSON.parse(res);
var ajax_list = []
console.log(records);

if (records === null)
    window.location.replace("/query");

var total = 0;

for (var i = 0; i < records.length; i++) {
    oj_name = records[i][0]
    username = records[i][1]
    // console.log(oj_name, username)
    ajax_list.push($.ajax({
        url: "/api/" + oj_name + "/" + username,
        type: "get",
        async: true,
        data: "",
        success: function (data) {
            var len = JSON.parse(JSON.parse(data).data).length
            var temp_list = this.url.split("/");
            var username = temp_list.pop();
            var oj_name = temp_list.pop();
            create_row(username+" on "+oj_name, len)
            total += len;
        }
    }));
}
const p = Promise.all(ajax_list);
p.then(res => {
    create_row("TOTAL:", total)
    console.log(total)
})
