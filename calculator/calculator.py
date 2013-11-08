__author__ = 'Micah'

from calculator import material_dicts

class GTC():
    """
    GTC(guitar tension calculator) is a class used to calculate the tension of a given string
    using the parameters: scale_length, string_material, gauge, note, octave.
    These parameters are defined in the constructor.
    """
    scale_length = 0
    unit_weight = 0
    freq = 0
    tension_constant = 386.4

    note_dict = {'C':       0,
                 'C#/Db':   1,
                 'D':       2,
                 'D#/Eb':   3,
                 'E':       4,
                 'F':       5,
                 'F#/Gb':   6,
                 'G':       7,
                 'G#/Ab':   8,
                 'A':       9,
                 'A#/Bb':   10,
                 'B':       11}



    def __init__(self, scale_length, string_material, gauge, note, octave):
        """
        Constructor for calculator class;
        initializes scale_length,
        frequency: using note and octave,
        and unit_weight: using string_material and gauge

        @param scale_length: the length of the guitar; used for string tension calculations
        @param string_material: the material the string is made of;
                                5 types due to the limited data provided by string manufacturers
                                used to calculate unit_weight
        @param gauge: the diameter of the string that is having its tension calculated
                        used to calculate the unit_weight
        @param note: the note the string is tuned to, one of the 12 notes possible; used to calculate the frequency
        @param octave: the octave of the note the string is being tuned to; used to calculate unit_weight
        """
        self.scale_length = scale_length
        self.freq = self.convert_to_freq(note, octave)
        self.unit_weight = self.convert_to_unit_weight(string_material, gauge)

    def calculate_tension(self):
        """
        Method of tension calculation provided by D'Addario
        @return: the calculated tension using  (UnitWeight x (2 x ScaleLength x Frequency)^2)/TensionConstant
        """
        tension = (self.unit_weight * (2*self.scale_length*self.freq)**2)/self.tension_constant
        #tension = float("{0:.2f}".format(tension))
        return tension

    def convert_to_halfsteps(self, note, octave):
        offset = 3
        base_octave = 5
        octave_offset = (octave - base_octave)*12
        note_offset = self.note_dict[note]
        return offset + octave_offset + note_offset

    def convert_to_freq(self, note, octave):
        """
        uses note and octave to calculate the frequency by using the dictionary of base frequencies
        Follows the equation: Frequency = BaseFrequncy * 2^Octave
        @param note: the note being converted to a frequency
        @param octave: the octave of the note being converted to a frequency
        @return: the frequency of the note and octave
        """
        half_steps = self.convert_to_halfsteps(note, octave)
        A4_freq = 440
        return A4_freq*(2**(1/12))**half_steps

    def convert_to_unit_weight(self, string_material, gauge):
        """
        cycles through an array of the appropriate string materials, comparing each entry to the gauge
        if the gauge in the reversed sorted list of keys is less than the given gauge then we have found
        the closest match our hardcoded dictionary values allow for
        @param string_material: one of 5 types used to determine which array to fetch
        @param gauge: the desired gauge, used to find the unit weight in the material_dict
        @return: the closest matched unit_weight to the gauge of the givin material
        """
        material_dict = material_dicts.get_material_dict(string_material)
        for g in reversed(sorted(material_dict.keys())):
            if g <= gauge:
                self.unit_weight = material_dict[g]
                return self.unit_weight
