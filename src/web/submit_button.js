

const e1 = React.createElement;

class SubmitButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { submit: false };
  }

  render() {
    if (this.state.submit) {
      return 'You submit this.';
    }

    return e(
      'button',
      { onClick: () => this.setState({ submit: true }) },
      'submit it '
    );
  }
}

const domContainer1 = document.querySelector('#submit_button_container');
const root1 = ReactDOM.createRoot(domContainer1);
root1.render(e1(SubmitButton));