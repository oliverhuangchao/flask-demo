function login_user() {
    var user_name = $("#user_name").val();
    var user_key = $("#user_key").val();
    $.ajax({
        type: "POST",
        url: "/loginchao",
        data: JSON.stringify({user_name: user_name, user_key: user_key}),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (resp) {
            if(!resp.result) {
                alert(resp.message);
            }else{
                window.location.replace("/dashboard");
            }
        },
        error: function (error) {
            console.log(error)
        }
    });
}

function create_new_user() {
    var user_name = $("#user_name").val();
    var user_key = $("#user_key").val();
    $.ajax({
        type: "POST",
        url: "/signup",
        data: JSON.stringify({user_name: user_name, user_key: user_key}),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (resp) {
            if(!resp.result) {
                alert(resp.message)
            }
            else{
                alert("already registered")
            }
        },
        error: function (error) {
            console.log(error)
        }
    });
}