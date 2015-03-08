#spontal_filter.py

import xml.etree.ElementTree as ET

def main():
    # lees vanuit bestand
    tree = ET.parse('spontal.xml')
    root = tree.getroot()
    
    # vind alle data van POINT
    for POINT in root.findall('POINT'):
        
        # get waarde van element
        BOTTOM = POINT.find('BOTTOM_HZ').text
        TOP = POINT.find('TOP_HZ').text
        START = POINT.find('F0_START').text
        END = POINT.find('F0_END').text
        
        # controleer of de F0 waarden tussen bottom en top waarde zitten, verijder foute data
        if BOTTOM >= float(START) >= float(TOP) or BOTTOM >= END >= TOP:
            root.remove(POINT)
    
    # schrijf alle goede data naar nieuwe bestand        
    tree.write('spontal_filtered.xml')
            
        
if __name__ == "__main__":
    main()
