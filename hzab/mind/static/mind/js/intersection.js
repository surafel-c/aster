  
 
const observer = new IntersectionObserver((entries)=> {
    entries.forEach((entry)=>{
        if(entry.isIntersecting){

            entry.target.classList.add("show");
            }
            else{
                entry.target.classList.remove('show');
            }
    });
});

const officialCard = document.querySelectorAll('.hidem');
officialCard.forEach((x)=>observer.observe(x));

