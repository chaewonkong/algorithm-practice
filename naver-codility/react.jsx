import React, { Component } from 'react';
import classnames from 'classnames';
// you should import `lodash` as a whole module
import lodash from 'lodash';

const ITEMS_API_URL = 'http://localhost:4000/data';
const DEBOUNCE_DELAY = 500;

// the exported component can be either a function or a class

const DEFAULT = "control"
const LOADING = "control is-loading"

export default class Autocomplete extends Component {

    state = { text: "", searchRes: [], className: "" }

    getSearchedRes = text => {
        this.setState({ className: LOADING })
        fetch(ITEMS_API_URL + `?q=${text}`).then(searchRes => this.setState({ searchRes, className: DEFAULT }))
    }

    onChangeText = e => this.setState({ text: e.target.value })

    renderList = () => {
        const { searchRes } = this.state
        return searchRes.map(item => <a className="list-item" onClick={this.props.onSelectItem}>{item}</a>)
    }

    componentDidUpdate(prevProps, prevState) {
        if (prevState.text !== this.state.text) {
            lodash.debounce(() => this.getSearchedRes(this.state.text), DEBOUNCE_DELAY)
        }
    }

    render() {
        return (
            <div className="wrapper">
                <div className="control">
                    <input type="text" className="input" onChange={e => this.onChangeText(e)} />
                </div>
                {this.state.searchRes.length ? (<div className="list is-hoverable">{this.renderList}</div>) : null}

            </div>
        );
    }
}