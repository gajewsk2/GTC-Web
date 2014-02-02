# [Stringulator](http://stringulator.herokuapp.com/)

When it comes to guitar and bass strings, balanced tension is crucial to speed and accuracy. Stringulator is a much-needed, modernized guitar string tension calculator. By using a tension calculator musicians can create custom tunings and tension "feels" for their particular instruments -- even for the most exotic of extended range guitars. It was originally based on [Bangzero's String Gauge Calculator](http://www.bangzero.org/stringtension/), which is a great tool, but beginning to feel dated. Our site allows for users to save string sets to their profiles for later reference and editing, view others string set creations, and is one of the only calculators available to handle multi-scale extended range instruments. 

Check out an example set here: [8 String Multi-Scale Set](http://stringulator.herokuapp.com/calculate/?string_set_name=8%20string%20set).

## Table of Contents

 - [Getting Started](#getting-started)
 - [Making a String Set](#making-a-string-set)
 - [Valid Inputs](#valid-inputs)
 - [Understanding Your Tension](#understanding-your-tension)
 - [What is Coming Next?](#what-is-coming-next)
 - [Bugs and Feature Requests](#bugs-and-feature-requests)
 - [Community](#community)
 - [Contribution](#contribution)
 - [Authors](#authors)
 
## Getting Started

- First click [Register](http://stringulator.herokuapp.com/accounts/register/) and make an account. While you do not have to be registered to make a string set, you do have to be registered and logged in to save a string set. 

- Next, login with the account you created.

## Making a String Set

- Click [Calculate](http://stringulator.herokuapp.com/calculate/).

- Fill out the form. If a parameter is green, then it is vaild; if a parameter is red it is invalid.

- Click Add String to add more strings to your set.

- Click Save Set to save the string set to your profile. If the site says string set saved then there were no errors and and you can view the set on your profile to review and edit it. A string set will still be saved if there is an invalid string in the set; the set will be saved while the invalid strings will be discarded.

## Valid Inputs

### Name
- A name must be less then 30 characters. 
- You can search for string sets based on name and use them as a template. 

### Description
- A description must be less then 1000 characters.
- A description will be searchable in a future version of the site.

### Multiscale
- Check the box if the string set is for a multi-scale scale length. This will reveal the box for Total Number of Strings.
- Leave the box unchecked if you have a standard scale length.

### Total Number of Strings
- This field only needs to be filled out if the guitar is multi-scale. It determines the width of the fret fanning for each string.

### Scale Length
- A standard scale length must be a number (usually with no more than 3 decimal places) less than 100.
- A multi-scale scale length must be two standard scale lengths joined with a hyphen: '-'. The smaller number typically comes first. Ex: 27-28.625

### Number
- The string number must be less than 100.
- The string number, is used for reference and does not make a difference on the tension calculation on a standard scale length.
- If the scale length is multi-scale, then this number must be no greater than the Total Number of Strings. This number is used to determine the relative standard scale length of a multi-scale neck.
- Typically, we say the highest string is the first and the lowest is greatest number. Ex: High E on guitar is 1; Low E on standard 6 string is 6

### Note
- The notes may be selected from the drop-down list, to correspond to the current strings note.

### Octave
- The octave says how high or low a note is and may be selected from the drop-down from number ranging through 1 to 9.

Example octaves from standard tuned 6 string:

- String 1 e: Octave 4

- String 2 B: Octave  3

- String 3 G: Octave 3

- String 4 D: Octave 3

- String 5 A: Octave 2

- String 6 E: Octave 2

For more info on how octaves work check out wikipedia's entry: [Octave](http://en.wikipedia.org/wiki/Octave)

### Gauge
- The gauge of the string must be less than 1.0 and have less than 6 decimal places.
- This is used to find the unit tension released by string manufacturers. If the string manufacturer did not release the unit tension for the gauge you input then the unit tension is approximated.

### String Type
- The string types can be selected from the drop-down menu. Currently only DiMarzio's five basic types are availible, but more will be added soon (including Circle K).

## Understanding Your Tension
- The basic idea is to get all of your strings tension as close as possible to the feel you want; obviously these fluctuate depending on the player but some general guidelines are:
- A light set averages 14 lbs of tension
- A medium set averages 16 lbs
- A heavy set averages 18 lbs
- Try to keep all strings to a tension of +- 1 lb of the average tension, but do not let the tension keep you from experimenting with what feels natural.

## What is Coming Next

Major:
- add javascript / descriptions of appropriate inputs - matt
- fix csrf verification
- fix mini nav bar
- add legit readme to github
- ajax save string set
- change export sets file name


Extra:
- circle k’s string tension values (parse into usable array, add parameters to dropdowns)
- add favicon
- add paypal donate button
- feedback on tension of set
- search by description
- have a sort button to arrange strings by number
- fix adding rows color(always shows last color)

Recently Done:
- calc tension on loading of saved set
- fix ajax verification
- add contact page
- add multiscale calculations (add description and total num as well) - micah
- save and load multiscale -micah
- fix info page -> change to link to our github
- fix register page - matt
- edit existing sets - micah
- ajax password check on register
- validate character length of client side input


## Bugs and Feature Requests

Have a bug or a feature request? Contact us at stringulator@gmail.com.

## Community

We are active on seven string forums  and will update this with a forum thread when we officially launch!

## Contributing

We would love to have you help us make a better guitar tension calculator! Contact us through stringulator@gmail.com, or at our active sevenstring forum thread


## Authors

**Micah Gajewski**

- [Resume](https://s3.amazonaws.com/recpass-production-resumes/resumes/documents/000/049/183/original/927adf9d518b81e5cc0ca84b0230dce21226c2e0.pdf?1391298580)
- <http://www.linkedin.com/in/micahgajewski>
- <https://github.com/gajewsk2>
- <https://www.facebook.com/micah.gajewski>

**Matt Lodes**

- <https://github.com/Matthew-L>



## License

A Team #TripleYoloSwagMoney Creation. Code released under the Mit License.
Stringulator to-do’s
