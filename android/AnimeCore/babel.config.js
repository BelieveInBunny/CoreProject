// eslint-disable-next-line func-names
module.exports = function (api) {
    api.cache(true);
    return {
        presets: ['babel-preset-expo'],
        plugins: [
            [
                'module-resolver',
                {
                    root: ['.'],
                    alias: {
                        '@assets': 'assets',
                    },
                },
            ],
            ['nativewind/babel'],
        ],
    };
};
