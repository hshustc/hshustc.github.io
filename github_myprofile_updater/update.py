if __name__ == '__main__':
    _header = '## Hi there 👋'
    base_dir = '../_pages/includes/'
    _intro = open(f'{base_dir}/1-intro.md', encoding='utf8').read().strip()
    with open('README.md', 'w', encoding='utf8') as f:
        f.write(_header)
        f.write('\n\n')
        f.write(_intro)
        f.write('\n\n')