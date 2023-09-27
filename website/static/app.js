const toggleBtn = document.getElementById("add-button");
const addSection = document.querySelector(".add-section");

toggleBtn.addEventListener("click", () => {
  addSection.classList.visibility = "visible";
  console.log(addSection.classList);
});
