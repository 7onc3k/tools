// Seznam textů pro vkládání
var textList = [
  "Doom",
  "Diablo",
  "Fortnite",
  "Minecraft",
  "The Witcher",
  "FIFA",
  "Call of Duty",
  "Cyberpunk 2077",
  "Grand Theft Auto",
  "Assassin's Creed",
  "Red Dead Redemption",
  "The Last of Us",
  "World of Warcraft",
  "League of Legends",
  "Counter-Strike"
];

// Funkce pro vložení textu a kliknutí na tlačítko
function fillAndClick() {
  var inputField = document.evaluate('/html/body/div[1]/div/div[1]/div/div[1]/div[1]/main/div/div/div/div[2]/div/div/div/div[1]/div/div/div/input', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
  var button = document.evaluate('/html/body/div[1]/div/div[1]/div/div[1]/div[1]/main/div/div/div/div[2]/div/div/div/div[1]/div/div/div/span/button', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;

  if (inputField && button) {
    var text = textList.shift();
    if (text) {
      inputField.value = text;
      button.disabled = false; // Odblokovat tlačítko
      button.click();
      setTimeout(fillAndClick, 1000); // Opakovat po 1 sekundě
    }
  }
}

// Spuštění funkce
fillAndClick();
