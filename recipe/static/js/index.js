const show_recipe = (el) => {
    console.log("Recipe switched");
    console.log(el);
    // Clear current recipe
    document.getElementById('recipe-ingredients-text').innerHTML = "";
    document.getElementById('recipe-directions-text').innerHTML = "";
    // Replace it with the ingredients/directions info inside the hidden HTML of the recipe cards
    document.getElementById('recipe-ingredients-text').innerHTML = el.querySelector('#recipe-ingredients').innerHTML;
    document.getElementById('recipe-directions-text').innerHTML  = el.querySelector('#recipe-directions').innerHTML;
    // Remove the opacity from placeholder text
    document.querySelector('#recipe-ingredients-text').style["opacity"] = "1"
    document.querySelector('#recipe-directions-text').style["opacity"] = "1"
}