$(document).ready(function () {
    $('#tool').tooltip();
    $('#searchtext').tooltip();
    $('#url').tooltip();
    $(".removecategory > h3>.label>.glyphicon ").css({
        "cursor": "select",
    });
    $(".removecategory > h3>.label ").on("mouseover", function () {

        $(this).css({

            "cursor": "pointer",
        });
    });


    $("select[name=linksperpage]").on("change", function () {

        var r = confirm("Changing link /page " + $(this).val());
        if (r == true) {



        }


    });


});


$(document).ready(function () {
    $("#csv").on("click", function () {
        $("#status").fadeIn().hide(1000);
    });
    $(".removecategory > h3 >.label ").on("click", function () {

        var r = confirm("Do you want to remove ?" + $(this).text());
        if (r == true) {

        }

    });
});


$(function () {
    $("#changeapassword").on("submit", function () {


        var current_password = $("#currentpassword").val();
        var password1 = $("#newpassword").val();
        var password2 = $("#newpasswordagain").val();

        if (current_password.length >= 6 && password1.length >= 6 && password2.length >= 6) {

            alert("here");
            if (current_password === password1 || current_password === password2) {
                $("#info").text("New and old password cannot be same");

            }
            return false;
        } else if (password1 != password2) {
            $("#info").text("Password Not Matched");
            return false;

        } else if (password1 === password2) {
            alert("After changing password  please login again to continue...");
            return true;
        } else {
            $("#info").text("Length > 6 ");
            return false;
        }
        return false;
    });
});

/**
 * Created by punit on 02-07-2017.
 */
