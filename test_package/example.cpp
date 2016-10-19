#include <iostream>
#include <tinyxml2/tinyxml2.h>

int main() {

    // just try to load the XML file should be enough
    // to verify that the linking and compiling works
    // correctly.
	tinyxml2::XMLDocument doc;
	doc.LoadFile("test.xml");

    std::cout<<"Parsed file: test.xml" << std::endl;
    return 0;
}
