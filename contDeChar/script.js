function countChar() {
    const textArea = document.getElementById("text-area");
    const charCount = document.getElementById("char-count");
    const text = textArea.value;
    charCount.textContent = `Número de caracteres: ${text.length}`;
}
