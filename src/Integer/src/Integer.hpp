#ifndef _BNUM_INTEGER_HPP_
#define _BNUM_INTEGER_HPP_

#include <string>

namespace Bnum
{
    class Integer
    {
        public:
            explicit        Integer ( const std::string& data = "0" );
            int             toInt ( void ) const;
        private:
            std::string     data;
    };
}

#endif  //  _BNUM_INTEGER_HPP_