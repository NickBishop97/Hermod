// Copyright 2016 Proyectos y Sistemas de Mantenimiento SL (eProsima).
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/*!
 * @file CLK.cpp
 * This source file contains the definition of the described types in the IDL file.
 *
 * This file was generated by the tool gen.
 */

#ifdef _WIN32
// Remove linker warning LNK4221 on Visual Studio
namespace {
char dummy;
}  // namespace
#endif  // _WIN32

#include "CLK.h"
#include <fastcdr/Cdr.h>

#include <fastcdr/exceptions/BadParamException.h>
using namespace eprosima::fastcdr::exception;

#include <utility>

CLK::CLK()
{
    // m_index com.eprosima.idl.parser.typecode.PrimitiveTypeCode@7fac631b
    m_index = 0;
    // m_clk com.eprosima.idl.parser.typecode.PrimitiveTypeCode@5b87ed94
    m_clk = 0;

}

CLK::~CLK()
{


}

CLK::CLK(
        const CLK& x)
{
    m_index = x.m_index;
    m_clk = x.m_clk;
}

CLK::CLK(
        CLK&& x)
{
    m_index = x.m_index;
    m_clk = x.m_clk;
}

CLK& CLK::operator =(
        const CLK& x)
{

    m_index = x.m_index;
    m_clk = x.m_clk;

    return *this;
}

CLK& CLK::operator =(
        CLK&& x)
{

    m_index = x.m_index;
    m_clk = x.m_clk;

    return *this;
}

bool CLK::operator ==(
        const CLK& x) const
{

    return (m_index == x.m_index && m_clk == x.m_clk);
}

bool CLK::operator !=(
        const CLK& x) const
{
    return !(*this == x);
}

size_t CLK::getMaxCdrSerializedSize(
        size_t current_alignment)
{
    size_t initial_alignment = current_alignment;


    current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4);


    current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4);



    return current_alignment - initial_alignment;
}

size_t CLK::getCdrSerializedSize(
        const CLK& data,
        size_t current_alignment)
{
    (void)data;
    size_t initial_alignment = current_alignment;


    current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4);


    current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4);



    return current_alignment - initial_alignment;
}

void CLK::serialize(
        eprosima::fastcdr::Cdr& scdr) const
{

    scdr << m_index;
    scdr << m_clk;

}

void CLK::deserialize(
        eprosima::fastcdr::Cdr& dcdr)
{

    dcdr >> m_index;
    dcdr >> m_clk;
}

/*!
 * @brief This function sets a value in member index
 * @param _index New value for member index
 */
void CLK::index(
        uint32_t _index)
{
    m_index = _index;
}

/*!
 * @brief This function returns the value of member index
 * @return Value of member index
 */
uint32_t CLK::index() const
{
    return m_index;
}

/*!
 * @brief This function returns a reference to member index
 * @return Reference to member index
 */
uint32_t& CLK::index()
{
    return m_index;
}

/*!
 * @brief This function sets a value in member clk
 * @param _clk New value for member clk
 */
void CLK::clk(
        uint32_t _clk)
{
    m_clk = _clk;
}

/*!
 * @brief This function returns the value of member clk
 * @return Value of member clk
 */
uint32_t CLK::clk() const
{
    return m_clk;
}

/*!
 * @brief This function returns a reference to member clk
 * @return Reference to member clk
 */
uint32_t& CLK::clk()
{
    return m_clk;
}


size_t CLK::getKeyMaxCdrSerializedSize(
        size_t current_alignment)
{
    size_t current_align = current_alignment;





    return current_align;
}

bool CLK::isKeyDefined()
{
    return false;
}

void CLK::serializeKey(
        eprosima::fastcdr::Cdr& scdr) const
{
    (void) scdr;
      
}
