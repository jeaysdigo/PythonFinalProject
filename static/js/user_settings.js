
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


