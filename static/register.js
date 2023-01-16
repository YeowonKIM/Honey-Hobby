// $(document).ready(function(){
//     userList = [] // 이메일 중복을 위해 기존 이메일을 받아올 리스트
//     get_user();
// })

function get_user(){
    $.ajax({
        type: 'GET', url: '/signin', data: {}, success: function (response) {
            userList = response.users
        }
    })
}

//회원가입 정보 저장, 유효성 검사
function save_account(){
    let id = $('#input-id').val()
    let password = $('#input-pw').val()
    let pw_confirm = $('#pw_confirm').val()

    if([id, password, pw_confirm].includes('')){
        alert('빈칸을 채워주세요')
        return;
    }

    //비밀번호 불일치 확인
    if(password !== pw_confirm){
        alert('비밀번호가 일치하지 않습니다')
        return;
    }

    //id 중복 제어
    for(let i=0; i<userList.length; i++){
        if(userList[i].id === id) {
            alert('이미 가입된 아이디입니다')
            return;
        }
    }

        $.ajax({
        type: 'POST',
        url: '/api/signup',
        data: {id_give: id, password_give: password},
        success: function (response) {
            alert(response['msg'])
            window.location.href = '/'
        }
    })

}
