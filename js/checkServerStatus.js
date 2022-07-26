const serverStatusParagraph = document.querySelector("#server-status");
const checkServerStatus = async () => {
    try {
        const { status } = await fetch("http://127.0.0.1:5000", { method: "GET" });
        if (status === 200) {
            serverStatusParagraph.style.color = "green";
            serverStatusParagraph.textContent = "Server is online!";
        }
        else {
            serverStatusParagraph.style.color = "red";
            serverStatusParagraph.textContent = "Server is offline!";
        }
        return status;
    }
    catch (err) {
        console.log(err);
        serverStatusParagraph.style.color = "red";
        serverStatusParagraph.textContent = "Server is offline!";
    }
};
export default checkServerStatus;
