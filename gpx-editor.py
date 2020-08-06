import getopt
import os
import sys

from lxml import etree

input_file_path = 'input_file.gpx'
output_file_path = 'output_file.gpx'
latitude = "0.000000"
longitude = "0.000000"


def parse_command_line_arguments():
    global input_file_path, output_file_path, lattitude, longitude
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["gpx=", "lat=", "lon="])
    except getopt.GetoptError:
        print('Wrong options, usage: gpx-editor.py --gpx <path to gpx file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == "--gpx":
            input_file_path = arg
            name, extension = os.path.splitext(input_file_path)
            output_file_path = name + "_edited" + extension
        if opt == "--lat":
            lattitude = arg
        if opt == "--lon":
            longitude = arg

    return input_file_path, output_file_path, lattitude, longitude


def save_file(xml_tree, file_path):
    with open(file_path, 'wb') as f:
        xml_tree.write(f)


def add_coords(xml_tree, longitude, latitude):
    for element in xml_tree.iter(tag="{http://www.topografix.com/GPX/1/1}trkpt"):
        element.set("lon", longitude)
        element.set("lat", latitude)


if __name__ == "__main__":
    parse_command_line_arguments()
    tree = etree.parse(input_file_path)
    add_coords(tree, longitude, latitude)
    save_file(xml_tree=tree, file_path=output_file_path)
