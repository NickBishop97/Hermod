#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE

#include <iostream>
#include <boost/test/unit_test.hpp>
#include "../Calculations.h"

#define INIT_VALUE 0.0
#define NEG_VALUE -0.001
#define ERROR_CODE -1.0
#define POS_VALUE 13.2354
#define DIFF_POS_VALUE 21.54
#define LARGER_THAN_TANK 0.001 + TANK_CAP
#define LARGE_FR 226754.6785576899 // Overflow testing*
#define LARGE_MPG 223654.6735786819

using namespace std;

/** 
 * @brief Assert that when MPG is negative, 
 * then get_MilesLeft returns ERROR_CODE 
 *
 * @param MPG Miles per Gallon
 * @param FR Fuel Remaining 
 * @return bool
 */
BOOST_AUTO_TEST_CASE(negativeMPG) 
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(NEG_VALUE, POS_VALUE) == ERROR_CODE);
}

/** 
 * @brief Assert that when MPG is 0 or init, 
 * then get_MilesLeft returns ERROR_CODE 
 *
 * @param MPG Miles per Gallon
 * @param FR Fuel Remaining 
 * @return bool
 */
BOOST_AUTO_TEST_CASE(zeroMPG) 
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(INIT_VALUE, POS_VALUE) == ERROR_CODE);
}

/** 
 * @brief Assert that when FR is 0 or init, 
 * then get_MilesLeft returns  
 *
 * @param MPG Miles per Gallon
 * @param FR Fuel Remaining 
 * @return bool
 */
BOOST_AUTO_TEST_CASE(zeroFR) 
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(POS_VALUE, INIT_VALUE) == ERROR_CODE);
}

/** 
 * @brief Assert that when FR is negative, 
 * then get_MilesLeft returns ERROR_CODE
 *
 * @param MPG Miles per Gallon
 * @param FR Fuel Remaining 
 * @return bool
 */
BOOST_AUTO_TEST_CASE(negtaiveFR) 
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(POS_VALUE, NEG_VALUE) == ERROR_CODE);
}

/** 
 * @brief Assert that when FR is larger than tank,  
 * then get_MilesLeft returns ERROR_CODE
 * @param MPG Miles per Gallon
 * @param FR Fuel Remaining 
 * @return bool
 */
BOOST_AUTO_TEST_CASE(excessiveFR) 
{
    ML ml;
    BOOST_CHECK(ml.get_MilesLeft(POS_VALUE, LARGER_THAN_TANK) == ERROR_CODE);
}

/** 
 * @brief Assert that when FR is larger than tank,  
 * then get_MilesLeft returns ERROR_CODE
 * @param MPG Miles per Gallon
 * @param FR Fuel Remaining 
 * @return bool
 */
BOOST_AUTO_TEST_CASE(overflow) 
{
    //ML ml;
    //BOOST_CHECK(ml.get_MilesLeft(POS_VALUE, LARGER_THAN_TANK) == ERROR_CODE);
}