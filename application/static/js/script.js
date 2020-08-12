//TUTORIAL: https://webdesign.tutsplus.com/tutorials/building-a-horizontal-timeline-with-css-and-javascript--cms-28378

(function() {

  //VARIABLES
  //document.queryselectorall = returns static nodelist of all document elements
  //that match selector inside the parenthesis
  //getting all the separate elements of the timeline from the css classes
  const timeline = document.querySelector(".timeline ol"),
  elH = document.querySelectorAll(".timeline li > div"),
  arrows = document.querySelectorAll(".timeline .arrows .arrow"),
  arrowPrev = document.querySelector(".timeline .arrows .arrow__prev"),
  arrowNext = document.querySelector(".timeline .arrows .arrow__next"),
  firstItem = document.querySelector(".timeline li:first-child"),
  lastItem = document.querySelector(".timeline li:last-child"),
  xScrolling = 280,
  disabledClass = "disabled";

  //STARTING THE CODE TO ANIMATE TIMELINE
  //call init when the entire page has loaded
  window.addEventListener("load", init); 

  function init() {
    setEqualHeights(elH);
    animateTl(xScrolling, arrows, timeline);
  }

  // SET EQUAL HEIGHTS
  function setEqualHeights(el) {
    let counter = 0;
    for (let i = 0; i < el.length; i++) {
      //get the height of the bubble and set to singleheight
      const singleHeight = el[i].offsetHeight;

      //if this singleheight is taller than counter, set counter to it
      if (counter < singleHeight) {
        counter = singleHeight;
      }
    }
    //set all the bubbles to the tallest height which is counter
    for (let i = 0; i < el.length; i++) {
      el[i].style.height = `${counter}px`;
    }
  }

  //CHECK IF AN ELEMENT IS IN VIEWPORT
  //http://stackoverflow.com/questions/123999/how-to-tell-if-a-dom-element-is-visible-in-the-current-viewport
  function isElementInViewport(el) {
    //size of the element and its poisiton relative to viewport
    const rect = el.getBoundingClientRect();
    //true if top, and left position is larger than zero and bottom is below innerheight and right is before the width
    return (
      rect.top >= 0 &&
      rect.left >= 0 &&
      rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
      rect.right <= (1100 || document.documentElement.clientWidth)
    );
  }

  //SET STATE OF PREV/NEXT ARROWS
  //if passed in flag is true, make it disabled, if false, make it not disabled
  function setBtnState(el, flag = true) {
    if (flag) {
      el.classList.add(disabledClass);
    } else {
      if (el.classList.contains(disabledClass)) {
        el.classList.remove(disabledClass);
      }
      el.disabled = false;
    }
  }

  //ANIMATE TIMELINE
  //function called by init, will call the other two functions
  //scrolling pixels, arrows, timeline
  function animateTl(scrolling, el, tl) {
    //listen to see if arrows are licked
    let counter = 0;
    for (let i = 0; i < el.length; i++) {
      el[i].addEventListener("click", function() {
        //disable once clicked
        if (!arrowPrev.disabled) {
          arrowPrev.disabled = true;
        }
        if (!arrowNext.disabled) {
          arrowNext.disabled = true;
        }
        //if prev, no sign, if next, - sign
        const sign = (this.classList.contains("arrow__prev")) ? "" : "-";
        //if first time transform to the right
        if (counter === 0) {
          tl.style.transform = `translateX(-${scrolling}px)`;
          //if not the first time, get current transform value and add or remove from it based on sign
        } else {
          const tlStyle = getComputedStyle(tl);
          // add more browser prefixes if needed here
          const tlTransform = tlStyle.getPropertyValue("-webkit-transform") || tlStyle.getPropertyValue("transform");
          const values = parseInt(tlTransform.split(",")[4]) + parseInt(`${sign}${scrolling}`);
          tl.style.transform = `translateX(${values}px)`;
        }

        setTimeout(() => {
          //if u see the first item, disable the prev button, if not don't disable the prev button
          isElementInViewport(firstItem) ? setBtnState(arrowPrev) : setBtnState(arrowPrev, false);
          //if u see the last item, disable the next button, if not, don't disable
          isElementInViewport(lastItem) ? setBtnState(arrowNext) : setBtnState(arrowNext, false);
        }, 1100);

        counter++;
      });
    }
  }

})();
