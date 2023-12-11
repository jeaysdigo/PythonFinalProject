function openChangeEmail() {
    document.body.classList.add("overflow-hidden");
    document.getElementById("changeEmailModal").classList.remove("invisible");
  }

  function closeChangeEmail() {
    document.body.classList.remove("overflow-hidden");
    document.getElementById("changeEmailModal").classList.add("invisible");
    document.getElementById("newEmail").value = "";
  }

  function openVerifyEmail() {
    document.body.classList.add("overflow-hidden");
    document.getElementById("verifyEmailModal").classList.remove("invisible");
    document.getElementById("changeEmailModal").classList.add("invisible");
  }

  function closeVerifyEmail() {
    document.body.classList.remove("overflow-hidden");
    document.getElementById("verifyEmailModal").classList.add("invisible");
    document.getElementById("enterNewEmail").value = "";
    document.getElementById("enterVerificationCode").value = "";
  }

  function openChangePassword() {
    document.body.classList.add("overflow-hidden");
    document.getElementById("changePassModal").classList.remove("invisible");
  }

  function closeChangePassword() {
    document.body.classList.remove("overflow-hidden");
    document.getElementById("changePassModal").classList.add("invisible");
    document.getElementById("oldPass").value = "";
    document.getElementById("newPass").value = "";
    document.getElementById("confirmPass").value = "";
  }

  function openDeleteAccount() {
    document.body.classList.add("overflow-hidden");
    document.getElementById("deleteAccountModal").classList.remove("invisible");
  }

  function closeDeleteAccount() {
    document.body.classList.remove("overflow-hidden");
    document.getElementById("deleteAccountModal").classList.add("invisible");
    document.getElementById("deleteEmail").value = "";
  }
  