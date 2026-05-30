// Highlight row on click and log data
document.addEventListener("DOMContentLoaded", () => {
    const rows = document.querySelectorAll("tbody tr");

    rows.forEach(row => {
        row.addEventListener("click", () => {
            // Remove previous highlights
            rows.forEach(r => r.style.backgroundColor = "");

            // Highlight current
            row.style.backgroundColor = "#d0ebff";

            // Log data (optional)
            const name = row.cells[0].innerText;
            const role = row.cells[1].innerText;
            const salary = row.cells[2].innerText;
            console.log(`Clicked: ${name} - ${role} - ${salary}`);
        });
    });
});
