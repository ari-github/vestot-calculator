function loadYear(select){
    select.innerHTML = ""
    const date = new KosherZmanim.JewishDate()
    var year = date.jewishYear - 2
    
    for (var i = 0; i < 10; i++){
        var opt = document.createElement('option');
        opt.value = year + i;
        opt.innerHTML = hdf.formatHebrewNumber(year + i);
        select.appendChild(opt);
    }
}

function loadMonth(select, year){
    select.innerHTML = ""
    const date = new KosherZmanim.JewishDate()
    date.setJewishYear(year)

    var monthNum = (date.isJewishLeapYear()) ? 13 : 12
    
    for (var i = 0; i < monthNum; i++){
        var opt = document.createElement('option');
        date.setJewishMonth(1 + i)

        opt.value = date.jewishMonth
        opt.innerHTML = hdf.formatMonth(date);
        if (i < 6){
            select.appendChild(opt)
        }else{
            select.insertBefore(opt, select.childNodes[i-6]);
        }
    }
}

function loadDay(select, year, month){
    select.innerHTML = ""
    const date = new KosherZmanim.JewishDate()
    date.setJewishYear(year)
    date.setJewishMonth(month)

    for (var i = 0; i < date.getDaysInJewishMonth(); i++){
        var opt = document.createElement('option');
        opt.value = 1 + i;
        opt.innerHTML = hdf.formatHebrewNumber(1 + i);
        select.appendChild(opt);
    }
}

const jd = new KosherZmanim.JewishDate();
const hdf = new KosherZmanim.HebrewDateFormatter();
hdf.setHebrewFormat(true)

selectYear = document.getElementById('year');
selectMonth = document.getElementById('month');
selectDay = document.getElementById('day');

loadYear(selectYear)
loadMonth(selectMonth, jd.jewishYear)
loadDay(selectDay, jd.jewishYear, jd.jewishMonth)

selectYear.value = jd.jewishYear
selectMonth.value = jd.jewishMonth
selectDay.value = jd.jewishDay

selectYear.onchange = () =>{
    loadMonth(selectMonth, selectYear.value)
    loadDay(selectDay, selectYear.value, selectMonth.value)

}
selectMonth.onchange = () =>{
    loadDay(selectDay, selectYear.value, selectMonth.value)
}
