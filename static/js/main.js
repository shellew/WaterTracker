const API_BASE_URL = "http://127.0.0.1:5000";

function setGoal() {
    const dailyGoal = document.getElementById("daily_goal").value;
    fetch(`${API_BASE_URL}/set_goal`, {
        method: "POST",
        header: { "Content-Type": "application/json" },
        body: JSON.stiringify({ daily_goal: dailyGoal })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        updateDisplay();
    })
    .catch(error => console.error("Error:", error))
}

function recordIntake() {
    const intakeAmount = document.getElementById("intake_amount").value;
    fetch(`${API_BASE_URL}/record_intake`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ intake_amount: intakeAmount })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        updateDisplay();        
    })
    .catch(error => console.error("Error:", error));
}

function resetIntake() {
    fetch(`${API_BASE_URL}/reset_intake`, { method: "POST" })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        updateDisplay();
    })
    .catch(error => console.error("Error", error));
}

function updateDisplay() {
    fetch(`${API_BASE_URL}/get_status`)
    .then(response => response.json())
    .then(data => {
        document.getElementById("display_goal").innerText = data.daily_goal;
        document.getElementById("display_total").innerText = data.total_intake;
    })
    .catch(error => console.error("Error", error));
}

window.onload = updateDisplay;