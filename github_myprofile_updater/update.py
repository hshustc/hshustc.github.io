if __name__ == '__main__':
    _header = '## Hi there'
    base_dir = '../_pages/includes/'
    _homepage = open(f'{base_dir}/homepage.md').read().strip()
    with open('README.md', 'w') as f:
        f.write(_header)
        f.write('\n\n')
        f.write(_homepage)