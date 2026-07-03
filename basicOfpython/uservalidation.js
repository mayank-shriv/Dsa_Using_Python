function usernameValidation(username){
    return /^[a-z]+$/.test(username)


}

console.log(usernameValidation('mayank'))