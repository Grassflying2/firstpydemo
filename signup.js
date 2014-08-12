/**
 * Created by t00202151 on 2014/8/12.
 */
$(document).ready(function () {
    $("form").submit(function (e) {
        var p1 = $("[name = 'signup_password']").val()
        var p2 = $("[name = 'repeated_password']").val()
        if (p1 != p2) {
            alert('两次密码不相同！')
            e.preventDefault();
        }
    });
});
