#ifndef _BNUM_INTEGER_HPP_
#define _BNUM_INTEGER_HPP_

#include <string>

namespace Bnum
{
    class Integer
    {
        public:
            explicit    Integer ( void ) = default;
            explicit    Integer ( const std::string& string );
            int         toInt ( void ) const;
    };
}

#endif  //  _BNUM_INTEGER_HPP_