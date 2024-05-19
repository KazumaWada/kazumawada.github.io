- React は component の塊でできている。
  component: html の要素等を返す function。これを export して実行する。
- 基本的な react の形

```js
// Step 1: Import React. This lets you use JSX inside your .js file.
import * as React from "react";

/* Step 2: Define your component. Note that your
component name should start with a capital letter. */
const MyComponent = () => {
  return <h1>Hi, welcome to my site!</h1>;
};

/* Step 3: Export your component so it
can be used by other parts of your app. */
export default MyComponent;
```

- top level の html 要素が 2 つあると、実行されない(h1 と p が div で囲われていたら ok)

```js
import * as React from 'react'

const ValidComponent = () => {
  return (
    <div>
      <h1>A valid component!</h1>
      <p>This will work fine.</p>
      <p>
        Since there is only one top-level element: the div.
      </p>
    </div>
  )
}

const InvalidComponent = () => {
  return (
    <h1>This won't work.</h1>
    <p>Because there are two elements at the top level.</p>
  )
}
```

## component 内に引数を入れるパターン

- props(properties):
  react's build in future to make components dynamic

```javascript
// Defining the <Greeting> component
const Greeting = (props) => {
  return <p>Hi {props.name}!</p>;
};

export default Greeting;

////export to this file↓////
import Greeting from "../components/greeting";

// Rendering the <Greeting> component
const SayHello = () => {
  return (
    <div>
      <Greeting name="Megan" /><--pops.name
      <Greeting name="Obinna" />
      <Greeting name="Generosa" />
    </div>
  );
};
```

## <Link>

```javascript
import * as React from "react";
import { Link } from "gatsby";

const IndexPage = () => {
  return (
    <main>
      <h1>Welcome to my Gatsby site!</h1>
      <Link to="/about">About</Link>
      <p>I'm making this by following the Gatsby Tutorial.</p>
    </main>
  );
};

export const Head = () => <title>Home Page</title>;

export default IndexPage;
```

## props を便利にしたもの/省略形

```javascript
//layout.js
import * as React from 'react'
import { Link } from 'gatsby'

const Layout = ({ pageTitle, children }) => {
  return (
    <div>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/about">About</Link></li>
        </ul>
      </nav>
      <main>
        <h1>{pageTitle}</h1>
        {children}
      </main>
    </div>
  )
}

export default Layout

//index.js
import Layout from '../components/layout'
const IndexPage = () => {
  return (
    <Layout pageTitle="Home Page">
      <p>I'm making this by following the Gatsby Tutorial.</p>
    </Layout>
  )
}

export const Head = () => <title>Home Page</title>

export default IndexPage
```

## how to add plugin to your site

install via npm
↓
add to gatsby-config.js
↓
import to your site

## GraphQL aka data layer(json 取得する前に見やすい画面で確認できる)

- 今までは手動で記事/画像を追加したりしていたけど、CMS(ContentsManagementSystem)を使った方が簡単にメインテナンスできる。なぜなら手動でやるよりコードの影響を与えないで update できるから。毎回手動で HTML 等を直接コードに記述しなくてはいけなくなるのを防ぐことができるから。拡張もしやすくなる。コンテンツを複数人で管理できるようになる。

DB,CMS,fileSystem
↓
GraphQL
↓
component

- graphQL 内で実行前に挙動を試すことができるから実装する時に予想しない挙動をしない。

##graphQL で確認したデータをコードに反映させる方法

- gatsby 専用の useStaticQuery というものがある。

```javascript
import * as React from "react";

// Gatsby専用のuseStaticQueryというのをimport
import { useStaticQuery, graphql } from "gatsby";

const Header = () => {
  /* Step 2: Use the useStaticQuery hook and
    graphql tag to query for data
    (The query gets run at build time) */
  const data = useStaticQuery(graphql`
    query {
      site {
        siteMetadata {
          title
        }
      }
    }
  `);

  return (
    <header>
      <h1>{data.site.siteMetadata.title}</h1>
    </header>
  );
};

export default Header;
```

##補足
graphQL で見たデータと、実際に impliment するデータは少し違う

```javascript
//graphQL
{
  "data": {
    "site": {
      "siteMetadata": {
        "title": "My First Gatsby Site"
      }
    }
  },
  "extensions": {}
}
//javascript
{
  "site": {
    "siteMetadata": {
      "title": "My First Gatsby Site"
    }
  }
}
```

## how to add new blog post

display title?
->graphQL から該当するデータを取ってきて、map で loop して表示する。

router?
->after got data shows title, create file src/pages/{data}.js.
ex, {mdx.frontmatter\_\_slug}.js
↓
go to localhost/data. done.
(data shoul be multiple lists, pick one.)

## how to create link for each blog post?

https://www.gatsbyjs.com/docs/tutorial/getting-started/part-6/
の Key GraphQL Concept: Query Variables を参考に
