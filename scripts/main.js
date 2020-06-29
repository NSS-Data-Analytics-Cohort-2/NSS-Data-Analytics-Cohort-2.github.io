
/** UTILITY FUNCTIONS **/
function loadData(fp, callback) {
  $.ajax({
    url: fp
  })
    .done(callback)
    .fail(function(error) {
      console.log("error", error);
    });
}

/**
 * Shuffles array in place.
 * @param {Array} a items An array containing the items.
 * Copied from https://stackoverflow.com/questions/6274339/how-can-i-shuffle-an-array#answer-6274381
 */
function shuffle(a) {
    var j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
    return a;
}

const disabled = (value) => value === null || value === "" ? "disabled" : "";


/** IMAGE TEMPLATES **/
const studentProImage = (record) => `<img class="card-img-top card-img-pro" src="${record.proImg}" alt="Pro Image" style="cursor:pointer;">`
const studentFunImage = (record) => `<img class="card-img-top card-img-fun" src="${record.funImg}" alt="Fun Image" style="cursor:pointer;">`


/** TEXT TEMPLATES **/
const studentName = (record) => `<h4 class="card-title title-font">${record.firstName} ${record.lastName}</h4>`
const studentReelThemIn = (record) => `<p class="card-text reelThemIn">${record.reelThemIn}</p>`
const studentBio = (record) => `<p class="card-text bio">${record.bio === null || record.bio === "" ? record.reelThemIn : record.bio}</p>`


/** ICON TEMPLATES **/
// if they don't have an href, don't display the icon.
const buildHREFIcon = (href, icon) => href == null ? `<a href=${href} target="_blank" class="disabled" disabled>${icon}</i></a>` : `<a href=${href} target="_blank">${icon}</i></a>`

const buildFabIcon = (label) => `<i class="fab fa-${label} fa-2x contactIcons"></i>`
const buildFasIcon = (label) => `<i class="fas fa-${label} fa-2x contactIcons"></i>`

const buildPortfolio = (href) => buildHREFIcon(href, buildFasIcon("globe"));
const buildGithub = (href) => buildHREFIcon(href, buildFabIcon("github"));
const buildLinkedin = (href) => buildHREFIcon(href, buildFabIcon("linkedin"));


/** BUTTON TEMPLATES **/
const studentResumeButton = (record) =>  `<a role="button" target="_blank" href="${record.resume}" aria-disabled="true" class="btn btn-default w-100 resumeButton cardActionButton title-font bottom ${disabled(record.resume)}" ${disabled(record.resume)}>Resume</a>`;
const studentCapstoneDemoButton = (record) => `<a role="button" target="_blank" href="${record.capstoneVideo}" aria-disabled="true" class="btn btn-default w-100 demoButton cardActionButton title-font bottom ${disabled(record.capstoneVideo)}" ${disabled(record.capstoneVideo)}>Demo</a>`;


/** HIRE ME TEMPLATE **/
const hireMe = (record) => record.job_searching === false ? "" : `<div class="hire-me">Hire me!</div>`;

/* PODCAST IFRAME */
const podcastIFrame = (record) => record.podcast === "" || record.podcast === null ? "" : record.podcast;


/** PROFILE CARD TEMPLATE **/
function buildCohortCard(record) {
  return `
<div class="col-md-3 d-flex flex-column cohortMems">
    ${hireMe(record)}
    ${studentProImage(record)}
    ${studentFunImage(record)}
    <div class="card-body cohortCard--studentInfo">
        ${studentName(record)}
        <div class="studentContact">
            ${buildGithub(record.github)}
            ${buildLinkedin(record.linkedin)}
            ${buildPortfolio(record.portfolio)}
        </div>
        <hr class="spacer">
        ${studentReelThemIn(record)}
        ${studentBio(record)}
    </div>
    <div class="mt-auto cohortCard--learnMore">
        ${podcastIFrame(record)}
        <div class="btn-group d-flex" role="group">
            ${studentResumeButton(record)}
            ${studentCapstoneDemoButton(record)}
        </div>
    </div>
</div>`;

}

/** TECHNOLOGIES TEMPLATE **/
function buildTech(record) {
  return `
  <div class="col-sm-2 technologies">
     <center>
       <a href="${record.link}" target="_blank"><img class="techs" src="${record.image}" alt="${record.name}" data-toggle="tooltip" data-placement="top" title="${record.name}"></a>
       <br>
     </center>
  </div>`;
}

/** COHORT CARDS ENTRY-POINT **/
function createCohortMembersVisuals(data) {
  let isJobSearching = data.filter((item) => item.job_searching === true);
  let isNotJobSearching = data.filter((item) => item.job_searching === false);

  // randomizing students
  shuffle(isJobSearching);
  shuffle(isNotJobSearching);

  isJobSearching.forEach((item) => document.getElementById("cohort").innerHTML += buildCohortCard(item));
  isNotJobSearching.forEach((item) => document.getElementById("cohort").innerHTML += buildCohortCard(item));
}

/** TECHNOLOGIES ENTRY-POINT **/
function createTechVisuals(list) {
  let data = list.techs;
  data.forEach((item) =>  document.getElementById("techs").innerHTML += buildTech(item));
}

/** ON PAGE LOAD **/
$(function() {
  loadData("data/cohort.json", createCohortMembersVisuals);
  loadData("data/techs.json", createTechVisuals);
});


// initialize the tool-tip plugin for Bootstrap4
$(function() {
  $('[data-toggle="tooltip"]').tooltip();
  $("#year").html(new Date().getFullYear());
  $(document).on("click", function() {
    $(".collapse").collapse("hide");
  });
});
