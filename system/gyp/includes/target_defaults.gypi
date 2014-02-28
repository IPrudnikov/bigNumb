{
    'target_defaults'   :   {
                                'include_dirs'      :   [
                                                            '<(STD_INCLUDE_DIR)',
                                                            '$(BNUM_HOME)/include',
                                                        ],
                                'sources'           :   [
                                                            '<@(UNIT_SOURCES)',
                                                        ],
                                'dependencies'      :   [
                                                            '<@(UNIT_DEPENDENCIES)',
                                                        ],
                                'cflags'            :   [
                                                            '<@(CFLAGS_STANDARD)',
                                                            '<@(UNIT_CFLAGS)',
                                                        ],
                                'ldflags'           :   [
                                                            '<@(LDFLAGS_STANDARD)',
                                                            '<@(UNIT_LDFLAGS)',
                                                        ],
                                'configurations'    :   {
                                                            'debug'     :   {
                                                                                'cflags'    :   [
                                                                                                    '<@(CFLAGS_DEBUG)',
                                                                                                ],
                                                                            },
                                                            'release'   :   {
                                                                                'cflags'    :   [
                                                                                                    '<@(CFLAGS_RELEASE)',
                                                                                                ],
                                                                            },
                                                        },
                            },
}