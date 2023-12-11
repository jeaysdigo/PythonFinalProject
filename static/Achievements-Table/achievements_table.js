document.addEventListener("DOMContentLoaded", function () {
  // Search functionality
  document.getElementById("searchInput").addEventListener("input", function () {
    const searchValue = this.value.toLowerCase().trim();
    const rows = document.querySelectorAll("#activityTable tbody tr");
    let hasResults = false;

    rows.forEach((row) => {
      const date = row.children[0].textContent.toLowerCase().trim();
      const studentName = row.children[1].textContent.toLowerCase().trim();
      const action = row.children[2].textContent.toLowerCase().trim();
      const description = row.children[3].textContent.toLowerCase().trim();

      const shouldShow =
        date.includes(searchValue) ||
        studentName.includes(searchValue) ||
        action.includes(searchValue) ||
        description.includes(searchValue);

      row.style.display = shouldShow ? "table-row" : "none";

      if (shouldShow) {
        hasResults = true;
      }
    });

    // Display a message when there are no search results
    const noResultsMessage = document.getElementById("noResultsMessage");
    if (hasResults) {
      noResultsMessage.style.display = "none";
    } else {
      noResultsMessage.style.display = "block";
    }
  });

  // Add even and odd row colors to the table
  const tableRows = document.querySelectorAll("#activityTable tbody tr");
  tableRows.forEach((row, index) => {
    // Use Tailwind CSS classes for even and odd row colors
    const colorClass = index % 2 === 0 ? "bg-gray-200" : "bg-white";
    row.classList.add(colorClass);
  });
});
