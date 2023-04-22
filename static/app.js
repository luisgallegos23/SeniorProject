function printdata(data){
    console.log(data);
}


function buildEventConfig(data){
    var val = 0;
    data.each(event => {
        var element = (
        `<label for="event-title">Event Title:</label>
        <input type="text" class="ininfo" id="event-title${val}" name="event-title" value="${event.summary}">

        <label for="start-date">Start Date:</label>
        <input type="date" class="ininfo" id="start-date${val}" name="start-date" value="${event.start.date}">

        <label for="start-time">Start Time:</label>
        <input type="time" class="ininfo" id="start-time${val}" name="start-time" value="">

        <label for="end-date">End Date:</label>
        <input type="date" class="ininfo" id="end-date${val}" name="end-date" value="${event.end.date}">

        <label for="end-time">End Time:</label>
        <input type="time" class="ininfo" id="end-time${val}" name="end-time" value="">

        <label for="description">Notes/Description:</label>
        <textarea id="description${val}" name="description" value=""></textarea>`
        )
        document.getElementById('config').innerHTML += element;
        val++;
    });

}