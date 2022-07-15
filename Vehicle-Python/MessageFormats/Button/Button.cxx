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
 * @file Button.cpp
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

#include "Button.h"
#include <fastcdr/Cdr.h>

#include <fastcdr/exceptions/BadParamException.h>
using namespace eprosima::fastcdr::exception;

#include <utility>

Button::Button()
{
    // m_index com.eprosima.idl.parser.typecode.PrimitiveTypeCode@7fac631b
    m_index = 0;
    // m_button com.eprosima.idl.parser.typecode.PrimitiveTypeCode@5b87ed94
    m_button = 0;

}

Button::~Button()
{


}

Button::Button(
        const Button& x)
{
    m_index = x.m_index;
    m_button = x.m_button;
}

Button::Button(
        Button&& x)
{
    m_index = x.m_index;
    m_button = x.m_button;
}

Button& Button::operator =(
        const Button& x)
{

    m_index = x.m_index;
    m_button = x.m_button;

    return *this;
}

Button& Button::operator =(
        Button&& x)
{

    m_index = x.m_index;
    m_button = x.m_button;

    return *this;
}

bool Button::operator ==(
        const Button& x) const
{

    return (m_index == x.m_index && m_button == x.m_button);
}

bool Button::operator !=(
        const Button& x) const
{
    return !(*this == x);
}

size_t Button::getMaxCdrSerializedSize(
        size_t current_alignment)
{
    size_t initial_alignment = current_alignment;


    current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4);


    current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4);



    return current_alignment - initial_alignment;
}

size_t Button::getCdrSerializedSize(
        const Button& data,
        size_t current_alignment)
{
    (void)data;
    size_t initial_alignment = current_alignment;


    current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4);


    current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4);



    return current_alignment - initial_alignment;
}

void Button::serialize(
        eprosima::fastcdr::Cdr& scdr) const
{

    scdr << m_index;
    scdr << m_button;

}

void Button::deserialize(
        eprosima::fastcdr::Cdr& dcdr)
{

    dcdr >> m_index;
    dcdr >> m_button;
}

/*!
 * @brief This function sets a value in member index
 * @param _index New value for member index
 */
void Button::index(
        uint32_t _index)
{
    m_index = _index;
}

/*!
 * @brief This function returns the value of member index
 * @return Value of member index
 */
uint32_t Button::index() const
{
    return m_index;
}

/*!
 * @brief This function returns a reference to member index
 * @return Reference to member index
 */
uint32_t& Button::index()
{
    return m_index;
}

/*!
 * @brief This function sets a value in member button
 * @param _button New value for member button
 */
void Button::button(
        uint32_t _button)
{
    m_button = _button;
}

/*!
 * @brief This function returns the value of member button
 * @return Value of member button
 */
uint32_t Button::button() const
{
    return m_button;
}

/*!
 * @brief This function returns a reference to member button
 * @return Reference to member button
 */
uint32_t& Button::button()
{
    return m_button;
}


size_t Button::getKeyMaxCdrSerializedSize(
        size_t current_alignment)
{
    size_t current_align = current_alignment;





    return current_align;
}

bool Button::isKeyDefined()
{
    return false;
}

void Button::serializeKey(
        eprosima::fastcdr::Cdr& scdr) const
{
    (void) scdr;
      
}
