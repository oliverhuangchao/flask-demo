// function create_new_user() {
//     var user_name = $("#user_name").value();
//     var user_key = $("#user_key").value();
//     $.ajax({
//         type: "POST",
//         url: "/signup",
//         data: JSON.stringify({user_name: user_name, user_key: user_key}),
//         contentType: "application/json; charset=utf-8",
//         dataType: "json",
//         success: function (resp) {
//         },
//         error: function (error) {
//             console.log(error)
//         }
//     });
// }