function addTask() {
    var taskText = document.getElementById("task").value;
    if (taskText !== "") {
        var taskList = document.getElementById("taskList");
        var li = document.createElement("li");
        li.innerHTML = `${taskText} <button class='btn btn-light' onclick='removeTask(this)'>Excluir</button>`;
        taskList.appendChild(li);
        document.getElementById("task").value = "";
    }
}

function removeTask(element) {
    element.parentElement.remove();
}
